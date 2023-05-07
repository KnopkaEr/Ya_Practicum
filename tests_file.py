import functions_diplom
import data_diplom

def test_get_order_by_track():
    track_number = functions_diplom.created_order(data_diplom.body_create_order).json()['track']
    resp = functions_diplom.get_order(track_number)
    assert resp.status_code == 200
