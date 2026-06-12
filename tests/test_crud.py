from api.crud import create_personal_input, creation_prediction

def test_create_personal_input(db_session):

    class FakeData:
        EXT_SOURCE_1 = 30
        EXT_SOURCE_2 = 40
        EXT_SOURCE_3 = 35
        INSTAL_AMT_PAYMENT_sum = 45
        AMT_CREDIT = 1000
        CC_AMT_BALANCE_mean = 36
        DAYS_BIRTH = 15
        AMT_ANNUITY = 20
        AMT_GOODS_PRICE = 1000
        DAYS_EMPLOYED = 25
        PREV_CNT_PAYMENT_mean = 250
        INSTAL_PAYMENT_DIFF_mean = 25
        DAYS_ID_PUBLISH = 35
        PREV_CNT_PAYMENT_max = 25
        INSTAL_AMT_PAYMENT_mean = 250
        POS_MONTHS_BALANCE_min = 25
        BUREAU_AMT_CREDIT_SUM_DEBT_mean = 30
        BUREAU_AMT_CREDIT_SUM_mean = 40
        BUREAU_DAYS_CREDIT_max = 35
        POS_SK_DPD_DEF_mean = 22

    personal = create_personal_input(
        db=db_session,
        data=FakeData()
    )

    assert personal.id is not None
    assert personal.AMT_CREDIT == 1000.0
    assert personal.AMT_ANNUITY == 20.0
    assert personal.EXT_SOURCE_1 == 30.0
        

from api.database import get_db

def test_get_db():
    db_gen = get_db()
    db = next(db_gen)
    
    assert db is not None
    
    db.close()
    
def test_db_integration(db_session):

    assert db_session is not None