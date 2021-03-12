import requests
import json

serverToken = 'AAAATIWbBNw:APA91bEqgFtElJ3hc6kHEuYshIdG5A_F2kGQLd7UR9gXYYSOShZVtmsnklIAfkCbvdK82IZLkJvhDgqAvd37lGydEfMy2lRTT1jAr3zpEA67kifsKFW8e5m4OGUP3V6g0fNrzmazB7gN'
deviceToken = 'egE9DpERROeoV7Szfu__v6:APA91bHE2RkhqqEhSEvfAgACb-tvWkmjohgeuSSdJyllMAbyIJjrLROQGWI6vWRqWorQucFvRUq2nV_aVi1xZ1QaH5RIcfnnFJ_1NcrRGaWgD7QvcuYMZ1nFQuQCEotXEAaaaSDUiASV'
#deviceToken = 'e43NM_lxSfOngTv37YffsZ:APA91bENmGEYCNa5s1nwPbKEnCsg8-Fg7zpViSismADLyc6E0GFxsfA4OF-AfR3zt1elNyAJpCcYBDzQLtRNS1HocjZlBtmDsg5Cmn37KALZ8iyY2Cvi-Id0cH96DY7VmRuueQ_ZwckG'

def enviar(titulo, body, pantalla):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken, }
    body = {
        'notification': {'title': titulo,
                         'body': body},
        'to': deviceToken,
        'priority': 'high',
        'data': {
          'Clave': pantalla,
        }
    }
    response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
    print(response.status_code)

    print(response.json())
