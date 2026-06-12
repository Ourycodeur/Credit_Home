### Création des tables nous aurons 2 tables les entrées, sorties
from sqlalchemy import Column, Integer, Float, String, JSON, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from api.database import Base

#Creation de la table des données d'entrée de l'employé 

class PersonalInputs(Base):

    __tablename__ = "personal_inputs"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    EXT_SOURCE_1 = Column(Float, nullable=False)
    EXT_SOURCE_2 = Column(Float, nullable=False)
    EXT_SOURCE_3 = Column(Float, nullable=False)

    INSTAL_AMT_PAYMENT_sum = Column(Float, nullable=False)
    AMT_CREDIT = Column(Float, nullable=False)
    CC_AMT_BALANCE_mean = Column(Float, nullable=False)
    DAYS_BIRTH = Column(Float, nullable=False)
    AMT_ANNUITY = Column(Float, nullable=False)
    AMT_GOODS_PRICE = Column(Float, nullable=False)
    DAYS_EMPLOYED = Column(Float, nullable=False)
    PREV_CNT_PAYMENT_mean = Column(Float, nullable=False)
    INSTAL_PAYMENT_DIFF_mean = Column(Float, nullable=False)
    DAYS_ID_PUBLISH = Column(Float, nullable=False)
    PREV_CNT_PAYMENT_max = Column(Float, nullable=False)
    INSTAL_AMT_PAYMENT_mean = Column(Float, nullable=False)
    POS_MONTHS_BALANCE_min = Column(Float, nullable=False)
    BUREAU_AMT_CREDIT_SUM_DEBT_mean = Column(Float, nullable=False)
    BUREAU_AMT_CREDIT_SUM_mean = Column(Float, nullable=False)
    BUREAU_DAYS_CREDIT_max = Column(Float, nullable=False)
    POS_SK_DPD_DEF_mean = Column(Float, nullable=False)

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    prediction = relationship(
        "PersonalOutputs",
        back_populates="input_data",
        uselist=False
    )
    
    
# Création de la tables de la sortie de la prédiction

class PersonalOutputs(Base):

    __tablename__ = "personal_outputs"

    id_output = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    personal_id = Column(
        Integer,
        ForeignKey("personal_inputs.id"),
        nullable=False
    )

    target = Column(
        Integer,
        nullable=False
    )

    probability = Column(
        Float,
        nullable=False
    )

    model_version = Column(
        String,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    input_data = relationship(
        "PersonalInputs",
        back_populates="prediction"
    )
    
    
