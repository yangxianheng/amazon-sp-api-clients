from dataclasses import dataclass
from typing import Dict, List


class MarketPlaces:
    """
    定义了亚马逊的所有渠道。
    
    不提供任何数据实例，所有操作均通过四个接口完成。
    """

    @dataclass
    class __Item:
        index: int
        country: str
        market_place: str
        endpoint: str
        oauth_endpoint: str

        @property
        def region(self):
            return {
                "https://sellingpartnerapi-na.amazon.com": "us-east-1",
                "https://sellingpartnerapi-fe.amazon.com": "us-west-2",
                "https://sellingpartnerapi-eu.amazon.com": "eu-west-1",
            }[self.endpoint]

        @property
        def sandbox_endpoint(self):
            return {
                "https://sellingpartnerapi-eu.amazon.com": 'https://sandbox.sellingpartnerapi-eu.amazon.com',
                "https://sellingpartnerapi-na.amazon.com": 'https://sandbox.sellingpartnerapi-na.amazon.com',
                "https://sellingpartnerapi-fe.amazon.com": 'https://sandbox.sellingpartnerapi-fe.amazon.com',
            }[self.endpoint]

    # Pay attention that the index will write to database and should not be edited!
    # The five digits:
    # 1:   amazon endpoint
    # 2-3: amazon market place
    # 4:   not set
    __data = {}
    for index, country, endpoint, market_place, oauth_endpoint in [
        (101, 'United Arab Emirates', 'https://sellingpartnerapi-eu.amazon.com', 'A2VIGQ35RCS4UG',
         'https://sellercentral.amazon.ae'),
        (102, 'Germany', 'https://sellingpartnerapi-eu.amazon.com', 'A1PA6795UKMFR9',
         'https://sellercentral-europe.amazon.com'),
        (103, 'Spain', 'https://sellingpartnerapi-eu.amazon.com', 'A1RKKUPIHCS9HS',
         'https://sellercentral-europe.amazon.com'),
        (104, 'France', 'https://sellingpartnerapi-eu.amazon.com', 'A13V1IB3VIYZZH',
         'https://sellercentral-europe.amazon.com'),
        (105, 'United Kingdom', 'https://sellingpartnerapi-eu.amazon.com', 'A1F83G8C2ARO7P',
         'https://sellercentral-europe.amazon.com'),
        (106, 'India', 'https://sellingpartnerapi-eu.amazon.com', 'A21TJRUUN4KGV',
         'https://sellercentral.amazon.in'),
        (107, 'Italy', 'https://sellingpartnerapi-eu.amazon.com', 'APJ6JRA9NG5V4',
         'https://sellercentral-europe.amazon.com'),
        (108, 'Netherlands', 'https://sellingpartnerapi-eu.amazon.com', 'A1805IZSGTT6HS',
         'https://sellercentral.amazon.nl'),
        (109, 'Sweden', 'https://sellingpartnerapi-eu.amazon.com', 'A2NODRKZP88ZB9',
         'https://sellercentral.amazon.se'),
        (110, 'Turkey', 'https://sellingpartnerapi-eu.amazon.com', 'A33AVAJ2PDY3EV',
         'https://sellercentral.amazon.com.tr'),
        (111, 'Poland', 'https://sellingpartnerapi-eu.amazon.com', 'A1C3SOZRARQ6R3',
         'https://vendorcentral.amazon.pl'),
        (201, 'Australia', 'https://sellingpartnerapi-fe.amazon.com', 'A39IBJ37TRP1C6',
         'https://sellercentral.amazon.com.au'),
        (202, 'Japan', 'https://sellingpartnerapi-fe.amazon.com', 'A1VC38T7YXB528',
         'https://sellercentral.amazon.co.jp'),
        (203, 'Singapore', 'https://sellingpartnerapi-fe.amazon.com', 'A19VAU5U5O7RUS',
         'https://sellercentral.amazon.sg'),
        (301, 'United States of America', 'https://sellingpartnerapi-na.amazon.com', 'ATVPDKIKX0DER',
         'https://sellercentral.amazon.com'),
        (302, 'Brazil', 'https://sellingpartnerapi-na.amazon.com', 'A2Q3Y263D00KWC',
         'https://sellercentral.amazon.com.br'),
        (303, 'Canada', 'https://sellingpartnerapi-na.amazon.com', 'A2EUQ1WTGCTBG2',
         'https://sellercentral.amazon.ca'),
        (304, 'Mexico', 'https://sellingpartnerapi-na.amazon.com', 'A1AM78C64UM0Y8',
         'https://sellercentral.amazon.com.mx'),
    ]:
        __data[index] = __Item(index=index, country=country, market_place=market_place, endpoint=endpoint,
                               oauth_endpoint=oauth_endpoint)

    __country_map: Dict[str, __Item] = {}
    __endpoint_map: Dict[str, List[__Item]] = {}
    __market_place_id_map: Dict[str, __Item] = {}

    # 这里采用lambda来规避命名空间的问题
    (lambda c, d: [c.setdefault(place.country, place) for place in d.values()])(__country_map, __data)
    (lambda m, d: [m.setdefault(place.market_place, place) for place in d.values()])(__market_place_id_map, __data)
    (lambda m, d: [m.setdefault(place.endpoint, []).append(place) for place in d.values()])(__endpoint_map, __data)

    def __init__(self):
        raise ValueError('这个类不可以实例化')

    @classmethod
    def all(cls):
        return cls.__data.values()

    @classmethod
    def get_by_index(cls, index: int):
        return cls.__data[index]

    @classmethod
    def get_by_country(cls, country: str):
        return cls.__country_map[country]

    @classmethod
    def get_by_endpoint(cls, endpoint: str):
        return cls.__endpoint_map[endpoint]

    @classmethod
    def get_by_market_place_id(cls, market_place_id: str):
        return cls.__market_place_id_map[market_place_id]
