from conftest import headers, url_charges, url_invoicing
import requests

agreement_id = 5335

body = {
  "agreementId": agreement_id,
  "onDate": "2021-01-01T00:00:00.000Z"
}

class TestChargingInvoicing():

  def test_remove_old(self, connect):
    cur = connect.cursor()

    # Удаление начислений и инвойсов
    cur.execute("""
        delete from qa.balance_transaction
        where id in
        (select transaction_id from qa.service_charge
        where service_id in
        (select id from qa.service where agreement_id=%(agreement_id)s;
        delete from qa.service_charge where service_id in (select id from qa.service where agreement_id=%(agreement_id)s;
        delete from qa.invoice where agreement_id=%(agreement_id)s""", {'agreement_id': agreement_id})



  def test_create_new_charging(self):
      response = requests.post(url_charges, json=body, headers=headers)

      print(response.status_code)
      print(response.text)
      assert response.status_code == 200

  def test_create_new_invoicing(self):
      response = requests.post(url_charges, json=body, headers=headers)

      print(response.status_code)
      print(response.text)
      assert response.status_code == 200