# -*- coding: utf-8 -*-
import scrapy


class HotelsSpider(scrapy.Spider):
    name = 'hotels'
    allowed_domains = ['www.booking.com']
    start_urls = ['https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaIwCiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKJgaGPBsACAdICJDYxMjIyNWQ1LWIxYzktNGIzOC1hZDVkLWEzZTdkNzk3ZmU1ZtgCBeACAQ&sid=f7f89b6cbcd71fc661559f18f129827c&aid=304142&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.html%3Faid%3D304142%3Blabel%3Dgen173nr-1FCAEoggI46AdIM1gEaIwCiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKJgaGPBsACAdICJDYxMjIyNWQ1LWIxYzktNGIzOC1hZDVkLWEzZTdkNzk3ZmU1ZtgCBeACAQ%3Bsid%3Df7f89b6cbcd71fc661559f18f129827c%3Btmpl%3Dsearchresults%3Bcheckin_month%3D4%3Bcheckin_monthday%3D1%3Bcheckin_year%3D2022%3Bcheckout_month%3D4%3Bcheckout_monthday%3D2%3Bcheckout_year%3D2022%3Bcity%3D-1955538%3Bclass_interval%3D1%3Bdest_id%3D-1955538%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bsrpvid%3Df96c79bdbc960170%3Bss%3DBrussels%3Bss_all%3D0%3Bssb%3Dempty%3Bsshis%3D0%3Bssne%3DBrussels%3Bssne_untouched%3DBrussels%26%3B&ss=Brussels&is_ski_area=0&ssne=Brussels&ssne_untouched=Brussels&city=-1955538&checkin_year=2022&checkin_month=3&checkin_monthday=1&checkout_year=2022&checkout_month=3&checkout_monthday=2&group_adults=2&group_children=0&no_rooms=1&from_sf=1&offset=0']

    def parse(self, response):
        hotel_list = response.xpath("//div[@class='_7192d3184']")
        for hotel in hotel_list:
            yield{
                "Name": hotel.xpath('.//a[@class="fb01724e5b"]/div[@data-testid="title"]/text()').get(),
                "Normal price": hotel.xpath('.//span[@class="_a11e76d75 _6b0bd403c"]/text()').get(),
                "Posted price": hotel.xpath('.//span[@class="fde444d7ef _e885fdc12"]/text()').get(),
                "Location": hotel.xpath('.//span[@data-testid="address"]/text()').get(),
                "Distance": hotel.xpath('.//span[@data-testid="distance"]/text()').get(),
                "Rating": hotel.xpath('.//div[@class="_9c5f726ff bd528f9ea6"]/text()').get(),
                "No_of_Reviews": hotel.xpath('.//div[@class="_4abc4c3d5 _1e6021d2f _6e869d6e0"]/text()').get(),
                "Room_Type": hotel.xpath('.//span[@class="_c5d12bf22"]/text()').get(),
                "Bed_Type": hotel.xpath('.//div[@class="_2075f7b46"]/div[@class="_4abc4c3d5"]/text()').get(),
                "Promoted_badge": hotel.xpath('.//span[@class="_4abc4c3d5 ffe1efcb1b _20015f850"]/span/text()').get(),
                "Free_cancellation": hotel.xpath('.//div[@class="_3abe99b47"]/text()').get(),
                "Subway Access": hotel.xpath(".//span[contains(text(),'Subway')]/text()").get(),
                "Breakfast": hotel.xpath('.//span[@class="c79699a040"]/text()').get(),
                "Availability": hotel.xpath('.//div[@class="a466256aae"]/text()').get(),
                "Susatainability": hotel.xpath('.//span[@class="_2c7126bf4"]/text()').get(),
                "URL": hotel.xpath('.//a[@data-testid="title-link"]/@href').get(),
                #"Beach_distance": hotel.xpath('.//span[@class="aa8aca3756"]/text()').get(),
            }

        num_list = list(range(25,326,25))
        for num in num_list:
            next_page = f"https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaIwCiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKJgaGPBsACAdICJDYxMjIyNWQ1LWIxYzktNGIzOC1hZDVkLWEzZTdkNzk3ZmU1ZtgCBeACAQ&sid=f7f89b6cbcd71fc661559f18f129827c&aid=304142&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.html%3Faid%3D304142%3Blabel%3Dgen173nr-1FCAEoggI46AdIM1gEaIwCiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKJgaGPBsACAdICJDYxMjIyNWQ1LWIxYzktNGIzOC1hZDVkLWEzZTdkNzk3ZmU1ZtgCBeACAQ%3Bsid%3Df7f89b6cbcd71fc661559f18f129827c%3Btmpl%3Dsearchresults%3Bcheckin_month%3D4%3Bcheckin_monthday%3D1%3Bcheckin_year%3D2022%3Bcheckout_month%3D4%3Bcheckout_monthday%3D2%3Bcheckout_year%3D2022%3Bcity%3D-1955538%3Bclass_interval%3D1%3Bdest_id%3D-1955538%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bsrpvid%3Df96c79bdbc960170%3Bss%3DBrussels%3Bss_all%3D0%3Bssb%3Dempty%3Bsshis%3D0%3Bssne%3DBrussels%3Bssne_untouched%3DBrussels%26%3B&ss=Brussels&is_ski_area=0&ssne=Brussels&ssne_untouched=Brussels&city=-1955538&checkin_year=2022&checkin_month=3&checkin_monthday=1&checkout_year=2022&checkout_month=3&checkout_monthday=2&group_adults=2&group_children=0&no_rooms=1&from_sf=1&offset={num}"
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
            })


