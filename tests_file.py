import functions_diplom


track_number = functions_diplom.created_order().json()['track']


def test_get_status():
    resp = functions_diplom.get_order(track_number)
    assert resp.status_code == 200
