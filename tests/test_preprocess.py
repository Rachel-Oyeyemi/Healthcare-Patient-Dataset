from pathlib import Path
import sys
import pandas as pd
sys.path.append(str(Path(__file__).resolve().parents[1]/"src"))
from preprocess import preprocess_dataframe


def test_preprocess_removes_duplicates_and_adds_features():
    row={"Name":"jANE DOE","Age":40,"Gender":"Female","Blood Type":"O+","Medical Condition":"Diabetes","Date of Admission":"2024-01-01","Doctor":"Dr. Alex Smith","Hospital":"Central Hospital,","Insurance Provider":"Aetna","Billing Amount":-15.123,"Room Number":201,"Admission Type":"Urgent","Discharge Date":"2024-01-05","Medication":"Aspirin","Test Results":"Normal"}
    output=preprocess_dataframe(pd.DataFrame([row,row]))
    assert len(output)==1
    assert output.loc[0,"name"]=="Jane Doe"
    assert output.loc[0,"billing_amount"]==-15.12
    assert output.loc[0,"is_negative_billing"]==1
    assert output.loc[0,"length_of_stay"]==4
    assert output.loc[0,"admission_id"]=="ADM-000001"
