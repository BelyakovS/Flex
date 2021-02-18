from conftest import headers, url_api
import requests

period_from = '2020-08-31'
agreement_id = 5335

body_charging = {
    'tariffTypeId': 9,
    'tariffStatusId': 9,
    'serviceTypeId': 9,
    'name': "test14",
    'currencyId': 9,
    'priceTypeId': 9,
    'priceUnitId': 9
}


class TestChargingInvoicing():

  def test_remove_old(self, connect):
    cur = connect.cursor()

    # cur.execute("SELECT * from qa.dic WHERE dic_type_id = %s", (dt_id,))

    # Удаление начислений и инвойсов
    cur.execute("""select * from qa.service_charge 
                    where service_id in (select id from qa.service where agreement_id=(%s)) 
                    and period_from > (%s)
                    order by transaction_id desc;""", (agreement_id, period_from,))

    # Печать значений из Селекта (не актуально)
    #rows = cur.fetchall()
    # print('\n')
    # for row in rows:
    #     print(row)

  def test_create_new_charging(self):
      response = requests.post(url_api, json=body_charging, headers=headers)

      print(response.status_code)
      print(response.text)
      assert response.status_code == 200