from main import f_geo_logs, geo_logs, f_ids, ids, f_stats, stats
import pytest


def test_geo_logs():
    expected_res = 'Россия'
    res = f_geo_logs(geo_logs)
    for values in res.values():
        assert expected_res in values

def test_ids():
    expected_res = [213, 15, 54, 119, 98, 35]
    res = f_ids(ids)
    for i in expected_res:
        assert i in res

def test_stats():
    expected_res = 'yandex'
    res = f_stats(stats)
    assert res == expected_res
