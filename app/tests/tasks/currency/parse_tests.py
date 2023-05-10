from currency.tasks import parse_privatbank, parse_monobank
from currency.models import Rate

from tests.utils.task_utils import get_request_mocker


def test_parse_privatbank(mocker):
    initial_count = Rate.objects.count()
    privat_data = [
        {
            "ccy": "EUR",
            "base_ccy": "UAH",
            "buy": "40.13220",
            "sale": "41.84100"},
        {
            "ccy": "USD",
            "base_ccy": "UAH",
            "buy": "36.56860",
            "sale": "37.45318"
         }
    ]
    request_get_mock = get_request_mocker(mocker, privat_data)  # noqa: F841
    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2
    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2


def test_parse_monobank(mocker):
    initial_count = Rate.objects.count()
    monobank_data = [
        {
            "currencyCodeA": 840,
            "currencyCodeB": 980,
            "date": 1682805674,
            "rateBuy": 36.65,
            "rateCross": 0,
            "rateSell": 37.4406
        },
        {
            "currencyCodeA": 978,
            "currencyCodeB": 980,
            "date": 1682805674,
            "rateBuy": 40.3,
            "rateCross": 0,
            "rateSell": 41.5007
        },
        {
            "currencyCodeA": 978,
            "currencyCodeB": 840,
            "date": 1682805674,
            "rateBuy": 1.094,
            "rateCross": 0,
            "rateSell": 1.107
        },
        {
            "currencyCodeA": 826,
            "currencyCodeB": 980,
            "date": 1682874676,
            "rateBuy": 0,
            "rateCross": 47.1081,
            "rateSell": 0
        },
        {
            "currencyCodeA": 392,
            "currencyCodeB": 980,
            "date": 1682874663,
            "rateBuy": 0,
            "rateCross": 0.2801,
            "rateSell": 0
        },
        {
            "currencyCodeA": 756,
            "currencyCodeB": 980,
            "date": 1682874630,
            "rateBuy": 0,
            "rateCross": 42.0617,
            "rateSell": 0
        },
        {
            "currencyCodeA": 156,
            "currencyCodeB": 980,
            "date": 1682874429,
            "rateBuy": 0,
            "rateCross": 5.4186,
            "rateSell": 0
        },
        {
            "currencyCodeA": 784,
            "currencyCodeB": 980,
            "date": 1682874628,
            "rateBuy": 0,
            "rateCross": 10.1974,
            "rateSell": 0
        },
        {
            "currencyCodeA": 971,
            "currencyCodeB": 980,
            "date": 1663425223,
            "rateBuy": 0,
            "rateCross": 0.4252,
            "rateSell": 0
        },
        {
            "currencyCodeA": 8,
            "currencyCodeB": 980,
            "date": 1682874677,
            "rateBuy": 0,
            "rateCross": 0.3725,
            "rateSell": 0
        },
        {
            "currencyCodeA": 51,
            "currencyCodeB": 980,
            "date": 1682874317,
            "rateBuy": 0,
            "rateCross": 0.0972,
            "rateSell": 0
        },
        {
            "currencyCodeA": 973,
            "currencyCodeB": 980,
            "date": 1682706808,
            "rateBuy": 0,
            "rateCross": 0.0737,
            "rateSell": 0
        },
        {
            "currencyCodeA": 32,
            "currencyCodeB": 980,
            "date": 1682874376,
            "rateBuy": 0,
            "rateCross": 0.1688,
            "rateSell": 0
        },
        {
            "currencyCodeA": 36,
            "currencyCodeB": 980,
            "date": 1682873727,
            "rateBuy": 0,
            "rateCross": 24.8804,
            "rateSell": 0
        },
        {
            "currencyCodeA": 944,
            "currencyCodeB": 980,
            "date": 1682874133,
            "rateBuy": 0,
            "rateCross": 22.024,
            "rateSell": 0
        },
        {
            "currencyCodeA": 50,
            "currencyCodeB": 980,
            "date": 1682873001,
            "rateBuy": 0,
            "rateCross": 0.353,
            "rateSell": 0
        },
        {
            "currencyCodeA": 975,
            "currencyCodeB": 980,
            "date": 1682874679,
            "rateBuy": 0,
            "rateCross": 21.1458,
            "rateSell": 0
        },
        {
            "currencyCodeA": 48,
            "currencyCodeB": 980,
            "date": 1682790071,
            "rateBuy": 0,
            "rateCross": 99.5931,
            "rateSell": 0
        },
        {
            "currencyCodeA": 108,
            "currencyCodeB": 980,
            "date": 1538606522,
            "rateBuy": 0,
            "rateCross": 0.0158,
            "rateSell": 0
        },
        {
            "currencyCodeA": 96,
            "currencyCodeB": 980,
            "date": 1681712199,
            "rateBuy": 0,
            "rateCross": 28.363,
            "rateSell": 0
        },
        {
            "currencyCodeA": 68,
            "currencyCodeB": 980,
            "date": 1682812661,
            "rateBuy": 0,
            "rateCross": 5.4588,
            "rateSell": 0
        },
        {
            "currencyCodeA": 986,
            "currencyCodeB": 980,
            "date": 1682874505,
            "rateBuy": 0,
            "rateCross": 7.5093,
            "rateSell": 0
        },
        {
            "currencyCodeA": 72,
            "currencyCodeB": 980,
            "date": 1681978995,
            "rateBuy": 0,
            "rateCross": 2.8521,
            "rateSell": 0
        },
        {
            "currencyCodeA": 933,
            "currencyCodeB": 980,
            "date": 1682865600,
            "rateBuy": 0,
            "rateCross": 12.7989,
            "rateSell": 0
        },
        {
            "currencyCodeA": 124,
            "currencyCodeB": 980,
            "date": 1682874674,
            "rateBuy": 0,
            "rateCross": 27.6686,
            "rateSell": 0
        },
        {
            "currencyCodeA": 976,
            "currencyCodeB": 980,
            "date": 1655462332,
            "rateBuy": 0,
            "rateCross": 0.0163,
            "rateSell": 0
        },
        {
            "currencyCodeA": 152,
            "currencyCodeB": 980,
            "date": 1682873578,
            "rateBuy": 0,
            "rateCross": 0.0465,
            "rateSell": 0
        },
        {
            "currencyCodeA": 170,
            "currencyCodeB": 980,
            "date": 1682872362,
            "rateBuy": 0,
            "rateCross": 0.008,
            "rateSell": 0
        },
        {
            "currencyCodeA": 188,
            "currencyCodeB": 980,
            "date": 1682872670,
            "rateBuy": 0,
            "rateCross": 0.0693,
            "rateSell": 0
        },
        {
            "currencyCodeA": 192,
            "currencyCodeB": 980,
            "date": 1682719206,
            "rateBuy": 0,
            "rateCross": 1.5237,
            "rateSell": 0
        },
        {
            "currencyCodeA": 203,
            "currencyCodeB": 980,
            "date": 1682874681,
            "rateBuy": 0,
            "rateCross": 1.7615,
            "rateSell": 0
        },
        {
            "currencyCodeA": 262,
            "currencyCodeB": 980,
            "date": 1678810696,
            "rateBuy": 0,
            "rateCross": 0.2108,
            "rateSell": 0
        },
        {
            "currencyCodeA": 208,
            "currencyCodeB": 980,
            "date": 1682874646,
            "rateBuy": 0,
            "rateCross": 5.5469,
            "rateSell": 0
        },
        {
            "currencyCodeA": 12,
            "currencyCodeB": 980,
            "date": 1682859523,
            "rateBuy": 0,
            "rateCross": 0.2768,
            "rateSell": 0
        },
        {
            "currencyCodeA": 818,
            "currencyCodeB": 980,
            "date": 1682874499,
            "rateBuy": 0,
            "rateCross": 1.2139,
            "rateSell": 0
        },
        {
            "currencyCodeA": 230,
            "currencyCodeB": 980,
            "date": 1682744552,
            "rateBuy": 0,
            "rateCross": 0.6876,
            "rateSell": 0
        },
        {
            "currencyCodeA": 981,
            "currencyCodeB": 980,
            "date": 1682874637,
            "rateBuy": 0,
            "rateCross": 15.1844,
            "rateSell": 0
        },
        {
            "currencyCodeA": 936,
            "currencyCodeB": 980,
            "date": 1682871644,
            "rateBuy": 0,
            "rateCross": 3.179,
            "rateSell": 0
        },
        {
            "currencyCodeA": 270,
            "currencyCodeB": 980,
            "date": 1682773982,
            "rateBuy": 0,
            "rateCross": 0.639,
            "rateSell": 0
        },
        {
            "currencyCodeA": 324,
            "currencyCodeB": 980,
            "date": 1682634561,
            "rateBuy": 0,
            "rateCross": 0.0044,
            "rateSell": 0
        },
        {
            "currencyCodeA": 344,
            "currencyCodeB": 980,
            "date": 1682866399,
            "rateBuy": 0,
            "rateCross": 4.7701,
            "rateSell": 0
        },
        {
            "currencyCodeA": 191,
            "currencyCodeB": 980,
            "date": 1680625280,
            "rateBuy": 0,
            "rateCross": 5.4258,
            "rateSell": 0
        },
        {
            "currencyCodeA": 348,
            "currencyCodeB": 980,
            "date": 1682874682,
            "rateBuy": 0,
            "rateCross": 0.111,
            "rateSell": 0
        },
        {
            "currencyCodeA": 360,
            "currencyCodeB": 980,
            "date": 1682874663,
            "rateBuy": 0,
            "rateCross": 0.0025,
            "rateSell": 0
        },
        {
            "currencyCodeA": 376,
            "currencyCodeB": 980,
            "date": 1682874657,
            "rateBuy": 0,
            "rateCross": 10.3435,
            "rateSell": 0
        },
        {
            "currencyCodeA": 356,
            "currencyCodeB": 980,
            "date": 1682874134,
            "rateBuy": 0,
            "rateCross": 0.4586,
            "rateSell": 0
        },
        {
            "currencyCodeA": 368,
            "currencyCodeB": 980,
            "date": 1682872060,
            "rateBuy": 0,
            "rateCross": 0.0285,
            "rateSell": 0
        },
        {
            "currencyCodeA": 364,
            "currencyCodeB": 980,
            "date": 1682719206,
            "rateBuy": 0,
            "rateCross": 0.0009,
            "rateSell": 0
        },
        {
            "currencyCodeA": 352,
            "currencyCodeB": 980,
            "date": 1682873683,
            "rateBuy": 0,
            "rateCross": 0.2763,
            "rateSell": 0
        },
        {
            "currencyCodeA": 400,
            "currencyCodeB": 980,
            "date": 1682874365,
            "rateBuy": 0,
            "rateCross": 52.8769,
            "rateSell": 0
        },
        {
            "currencyCodeA": 404,
            "currencyCodeB": 980,
            "date": 1682872856,
            "rateBuy": 0,
            "rateCross": 0.2754,
            "rateSell": 0
        },
        {
            "currencyCodeA": 417,
            "currencyCodeB": 980,
            "date": 1682873005,
            "rateBuy": 0,
            "rateCross": 0.4281,
            "rateSell": 0
        },
        {
            "currencyCodeA": 116,
            "currencyCodeB": 980,
            "date": 1682867187,
            "rateBuy": 0,
            "rateCross": 0.0091,
            "rateSell": 0
        },
        {
            "currencyCodeA": 408,
            "currencyCodeB": 980,
            "date": 1682719206,
            "rateBuy": 0,
            "rateCross": 16.6221,
            "rateSell": 0
        },
        {
            "currencyCodeA": 410,
            "currencyCodeB": 980,
            "date": 1682873505,
            "rateBuy": 0,
            "rateCross": 0.028,
            "rateSell": 0
        },
        {
            "currencyCodeA": 414,
            "currencyCodeB": 980,
            "date": 1682862683,
            "rateBuy": 0,
            "rateCross": 122.43,
            "rateSell": 0
        },
        {
            "currencyCodeA": 398,
            "currencyCodeB": 980,
            "date": 1682874500,
            "rateBuy": 0,
            "rateCross": 0.0828,
            "rateSell": 0
        },
        {
            "currencyCodeA": 418,
            "currencyCodeB": 980,
            "date": 1682854997,
            "rateBuy": 0,
            "rateCross": 0.0021,
            "rateSell": 0
        },
        {
            "currencyCodeA": 422,
            "currencyCodeB": 980,
            "date": 1678882171,
            "rateBuy": 0,
            "rateCross": 0.0004,
            "rateSell": 0
        },
        {
            "currencyCodeA": 144,
            "currencyCodeB": 980,
            "date": 1682870777,
            "rateBuy": 0,
            "rateCross": 0.1173,
            "rateSell": 0
        },
        {
            "currencyCodeA": 434,
            "currencyCodeB": 980,
            "date": 1674670757,
            "rateBuy": 0,
            "rateCross": 7.8783,
            "rateSell": 0
        },
        {
            "currencyCodeA": 504,
            "currencyCodeB": 980,
            "date": 1682864589,
            "rateBuy": 0,
            "rateCross": 3.7184,
            "rateSell": 0
        },
        {
            "currencyCodeA": 498,
            "currencyCodeB": 980,
            "date": 1682874646,
            "rateBuy": 0,
            "rateCross": 2.0922,
            "rateSell": 0
        },
        {
            "currencyCodeA": 969,
            "currencyCodeB": 980,
            "date": 1682183421,
            "rateBuy": 0,
            "rateCross": 0.0085,
            "rateSell": 0
        },
        {
            "currencyCodeA": 807,
            "currencyCodeB": 980,
            "date": 1682874090,
            "rateBuy": 0,
            "rateCross": 0.6681,
            "rateSell": 0
        },
        {
            "currencyCodeA": 496,
            "currencyCodeB": 980,
            "date": 1682841300,
            "rateBuy": 0,
            "rateCross": 0.0107,
            "rateSell": 0
        },
        {
            "currencyCodeA": 478,
            "currencyCodeB": 980,
            "date": 1682719206,
            "rateBuy": 0,
            "rateCross": 0.1076,
            "rateSell": 0
        },
        {
            "currencyCodeA": 480,
            "currencyCodeB": 980,
            "date": 1682872759,
            "rateBuy": 0,
            "rateCross": 0.8349,
            "rateSell": 0
        },
        {
            "currencyCodeA": 454,
            "currencyCodeB": 980,
            "date": 1678369785,
            "rateBuy": 0,
            "rateCross": 0.0368,
            "rateSell": 0
        },
        {
            "currencyCodeA": 484,
            "currencyCodeB": 980,
            "date": 1682874669,
            "rateBuy": 0,
            "rateCross": 2.0836,
            "rateSell": 0
        },
        {
            "currencyCodeA": 458,
            "currencyCodeB": 980,
            "date": 1682873155,
            "rateBuy": 0,
            "rateCross": 8.41,
            "rateSell": 0
        },
        {
            "currencyCodeA": 943,
            "currencyCodeB": 980,
            "date": 1682861232,
            "rateBuy": 0,
            "rateCross": 0.5848,
            "rateSell": 0
        },
        {
            "currencyCodeA": 516,
            "currencyCodeB": 980,
            "date": 1682862536,
            "rateBuy": 0,
            "rateCross": 2.0517,
            "rateSell": 0
        },
        {
            "currencyCodeA": 566,
            "currencyCodeB": 980,
            "date": 1682871180,
            "rateBuy": 0,
            "rateCross": 0.0808,
            "rateSell": 0
        },
        {
            "currencyCodeA": 558,
            "currencyCodeB": 980,
            "date": 1682793327,
            "rateBuy": 0,
            "rateCross": 1.029,
            "rateSell": 0
        },
        {
            "currencyCodeA": 578,
            "currencyCodeB": 980,
            "date": 1682874617,
            "rateBuy": 0,
            "rateCross": 3.5444,
            "rateSell": 0
        },
        {
            "currencyCodeA": 524,
            "currencyCodeB": 980,
            "date": 1682864041,
            "rateBuy": 0,
            "rateCross": 0.2865,
            "rateSell": 0
        },
        {
            "currencyCodeA": 554,
            "currencyCodeB": 980,
            "date": 1682866292,
            "rateBuy": 0,
            "rateCross": 23.1669,
            "rateSell": 0
        },
        {
            "currencyCodeA": 512,
            "currencyCodeB": 980,
            "date": 1682872180,
            "rateBuy": 0,
            "rateCross": 97.3221,
            "rateSell": 0
        },
        {
            "currencyCodeA": 604,
            "currencyCodeB": 980,
            "date": 1682874091,
            "rateBuy": 0,
            "rateCross": 10.1089,
            "rateSell": 0
        },
        {
            "currencyCodeA": 608,
            "currencyCodeB": 980,
            "date": 1682868225,
            "rateBuy": 0,
            "rateCross": 0.6764,
            "rateSell": 0
        },
        {
            "currencyCodeA": 586,
            "currencyCodeB": 980,
            "date": 1682874637,
            "rateBuy": 0,
            "rateCross": 0.1321,
            "rateSell": 0
        },
        {
            "currencyCodeA": 985,
            "currencyCodeB": 980,
            "date": 1682874680,
            "rateBuy": 0,
            "rateCross": 9.0444,
            "rateSell": 0
        },
        {
            "currencyCodeA": 600,
            "currencyCodeB": 980,
            "date": 1682874011,
            "rateBuy": 0,
            "rateCross": 0.0051,
            "rateSell": 0
        },
        {
            "currencyCodeA": 634,
            "currencyCodeB": 980,
            "date": 1682873158,
            "rateBuy": 0,
            "rateCross": 10.2854,
            "rateSell": 0
        },
        {
            "currencyCodeA": 946,
            "currencyCodeB": 980,
            "date": 1682874678,
            "rateBuy": 0,
            "rateCross": 8.3978,
            "rateSell": 0
        },
        {
            "currencyCodeA": 941,
            "currencyCodeB": 980,
            "date": 1682874669,
            "rateBuy": 0,
            "rateCross": 0.3529,
            "rateSell": 0
        },
        {
            "currencyCodeA": 682,
            "currencyCodeB": 980,
            "date": 1682873213,
            "rateBuy": 0,
            "rateCross": 9.9874,
            "rateSell": 0
        },
        {
            "currencyCodeA": 690,
            "currencyCodeB": 980,
            "date": 1682868893,
            "rateBuy": 0,
            "rateCross": 2.7553,
            "rateSell": 0
        },
        {
            "currencyCodeA": 938,
            "currencyCodeB": 980,
            "date": 1680961561,
            "rateBuy": 0,
            "rateCross": 0.0627,
            "rateSell": 0
        },
        {
            "currencyCodeA": 752,
            "currencyCodeB": 980,
            "date": 1682874665,
            "rateBuy": 0,
            "rateCross": 3.657,
            "rateSell": 0
        },
        {
            "currencyCodeA": 702,
            "currencyCodeB": 980,
            "date": 1682870008,
            "rateBuy": 0,
            "rateCross": 28.0872,
            "rateSell": 0
        },
        {
            "currencyCodeA": 694,
            "currencyCodeB": 980,
            "date": 1664217991,
            "rateBuy": 0,
            "rateCross": 0.0024,
            "rateSell": 0
        },
        {
            "currencyCodeA": 706,
            "currencyCodeB": 980,
            "date": 1682719206,
            "rateBuy": 0,
            "rateCross": 0.0647,
            "rateSell": 0
        },
        {
            "currencyCodeA": 968,
            "currencyCodeB": 980,
            "date": 1680879569,
            "rateBuy": 0,
            "rateCross": 1.0284,
            "rateSell": 0
        },
        {
            "currencyCodeA": 760,
            "currencyCodeB": 980,
            "date": 1682719206,
            "rateBuy": 0,
            "rateCross": 0.0056,
            "rateSell": 0
        },
        {
            "currencyCodeA": 748,
            "currencyCodeB": 980,
            "date": 1668614714,
            "rateBuy": 0,
            "rateCross": 2.1898,
            "rateSell": 0
        },
        {
            "currencyCodeA": 764,
            "currencyCodeB": 980,
            "date": 1682874680,
            "rateBuy": 0,
            "rateCross": 1.1006,
            "rateSell": 0
        },
        {
            "currencyCodeA": 972,
            "currencyCodeB": 980,
            "date": 1682861050,
            "rateBuy": 0,
            "rateCross": 3.4299,
            "rateSell": 0
        },
        {
            "currencyCodeA": 795,
            "currencyCodeB": 980,
            "date": 1682719206,
            "rateBuy": 0,
            "rateCross": 0.0021,
            "rateSell": 0
        },
        {
            "currencyCodeA": 788,
            "currencyCodeB": 980,
            "date": 1682871065,
            "rateBuy": 0,
            "rateCross": 12.3116,
            "rateSell": 0
        },
        {
            "currencyCodeA": 949,
            "currencyCodeB": 980,
            "date": 1682874681,
            "rateBuy": 0,
            "rateCross": 1.9455,
            "rateSell": 0
        },
        {
            "currencyCodeA": 901,
            "currencyCodeB": 980,
            "date": 1682874488,
            "rateBuy": 0,
            "rateCross": 1.2185,
            "rateSell": 0
        },
        {
            "currencyCodeA": 834,
            "currencyCodeB": 980,
            "date": 1682856590,
            "rateBuy": 0,
            "rateCross": 0.0159,
            "rateSell": 0
        },
        {
            "currencyCodeA": 800,
            "currencyCodeB": 980,
            "date": 1682869021,
            "rateBuy": 0,
            "rateCross": 0.01,
            "rateSell": 0
        },
        {
            "currencyCodeA": 858,
            "currencyCodeB": 980,
            "date": 1682872580,
            "rateBuy": 0,
            "rateCross": 0.9643,
            "rateSell": 0
        },
        {
            "currencyCodeA": 860,
            "currencyCodeB": 980,
            "date": 1682874404,
            "rateBuy": 0,
            "rateCross": 0.0032,
            "rateSell": 0
        },
        {
            "currencyCodeA": 937,
            "currencyCodeB": 980,
            "date": 1682719206,
            "rateBuy": 0,
            "rateCross": 1.4812,
            "rateSell": 0
        },
        {
            "currencyCodeA": 704,
            "currencyCodeB": 980,
            "date": 1682871539,
            "rateBuy": 0,
            "rateCross": 0.0015,
            "rateSell": 0
        },
        {
            "currencyCodeA": 950,
            "currencyCodeB": 980,
            "date": 1682844341,
            "rateBuy": 0,
            "rateCross": 0.0627,
            "rateSell": 0
        },
        {
            "currencyCodeA": 952,
            "currencyCodeB": 980,
            "date": 1682856364,
            "rateBuy": 0,
            "rateCross": 0.0627,
            "rateSell": 0
        },
        {
            "currencyCodeA": 886,
            "currencyCodeB": 980,
            "date": 1543715495,
            "rateBuy": 0,
            "rateCross": 0.112,
            "rateSell": 0
        },
        {
            "currencyCodeA": 710,
            "currencyCodeB": 980,
            "date": 1682874039,
            "rateBuy": 0,
            "rateCross": 2.05,
            "rateSell": 0
        },
        {
            "currencyCodeA": 894,
            "currencyCodeB": 980,
            "date": 1682719206,
            "rateBuy": 0,
            "rateCross": 0.0021,
            "rateSell": 0}
    ]
    request_get_mock = get_request_mocker(mocker, monobank_data)  # noqa: F841
    parse_monobank()
    assert Rate.objects.count() == initial_count + 2
    parse_monobank()
    assert Rate.objects.count() == initial_count + 2
