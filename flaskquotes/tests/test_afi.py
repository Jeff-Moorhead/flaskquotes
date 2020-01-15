from unittest import TestCase, mock
from bs4 import BeautifulSoup
from .. import afi


# TODO: unit test http connection


class TestFetchQuotes(TestCase):
    def setUp(self):
        self.test_html = """
        <div class="row"><div class="single_list col-sm-12 movie_popup" data-id="1751104"> <div 
        class="row"> <div class="col-sm-6"> <!--<img 
        src="https://www.afi.com/wp-content/themes/AFI/images/default.png" alt="GONE WITH THE WIND" />--> <div 
        class="m_head"> <h6 class="q_title"> 1. "Frankly, my dear, I don't give a damn."</h6> <a class="movie-detail" 
        href="javascript:void(0);">GONE WITH THE WIND <span>(1940)</span></a> </div> </div> <div class="col-sm-6"> <p 
        class="Cast"><span>Cast: </span>Thomas Mitchell, Barbara O'Neil, Vivien Leigh</p><p 
        class="Directors"><span>Directors: </span>Victor Fleming </p><p class="Producer"><span>Producer: </span>David 
        O. Selznick </p> <p class="Writer"><span> Writer: </span>Sidney Howard </p><p 
        class="Cinematographer"><span>Cinematographer: </span>Lee Garmes </p> <p 
        class="ProductionCompany"><span>Production Company: </span>Selznick International Pictures, Inc.</p> </div> 
        </div></div></div>"""

        self.quote_tag = """
        <div class="single_list col-sm-12 movie_popup" data-id="1751104">
          <div class="row">
            <div class="col-sm-6"> 
              <!--<img src="https://www.afi.com/wp-content/themes/AFI/images/default.png" alt="GONE WITH THE WIND" />-->
              <div class="m_head">
                <h6 class="q_title"> 1. "Frankly, my dear, I don't give a damn."</h6> 
                <a class="movie-detail" href="javascript:void(0);">GONE WITH THE WIND <span>(1940)</span></a>
              </div>
            </div>
            <div class="col-sm-6">
              <p class="Cast"><span>Cast: </span>Thomas Mitchell, Barbara O'Neil, Vivien Leigh</p>
              <p class="Directors"><span>Directors: </span>Victor Fleming </p>
              <p class="Producer"><span>Producer: </span>David O. Selznick </p>
              <p class="Writer"><span> Writer: </span>Sidney Howard </p>
              <p class="Cinematographer"><span>Cinematographer: </span>Lee Garmes </p>
              <p class="ProductionCompany"><span>Production Company: </span>Selznick International Pictures, Inc.</p>
            </div>
          </div>
        </div>"""

        self.soup = BeautifulSoup(self.test_html, "html.parser")
        self.quotes = self.soup.select('div.single_list.col-sm-12.movie_popup')
        self.maxDiff = None

    @mock.patch('requests.get')
    @mock.patch('requests.Response')
    def test_fetch_html(self, req_mock, response_mock):
        response = response_mock()
        response.text = self.test_html
        req_mock.return_value = response
        webpage = afi.fetch_afi_quotes_html()
        self.assertEqual(webpage.text, self.test_html)

    def test_find_quotes(self):
        quotes_from_func = afi.find_quotes(self.test_html)
        self.assertListEqual(quotes_from_func, self.quotes)

    def test_pack_quotes(self):
        quote_from_func = afi.pack_quotes(self.quotes, quote='h6.q_title', movie='a.movie-detail')
        packed_quote = {"1": {"Quote": '"Frankly, my dear, I don\'t give a damn."', "Movie": "Gone With The Wind",
                              "Year": "1940"}
                              }
        self.assertEqual(quote_from_func, packed_quote)
