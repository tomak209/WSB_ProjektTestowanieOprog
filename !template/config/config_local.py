from prestashop_app.prestashop_app_config import PrestashopAppConfig


config = PrestashopAppConfig()
config.driver_name = "firefox"
config.host = "http://www.mediamarkt.pl" #"http://demo.prestashop.com/?_ga#/en/front"
config.users_data = [{"title": "Mr.",
                      "first_name": "Wsb",
                      "last_name": "Tester",
                      "email": "tester@wsb.wroclaw.pl",
                      "password": "tester123"},
                     ]
