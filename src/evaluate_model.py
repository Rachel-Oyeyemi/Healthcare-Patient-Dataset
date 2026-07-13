"""Evaluate trained multiclass models and persist machine-readable metrics."""
from __future__ import annotations
import argparse
from pathlib import Path
import joblib
import numpy as np
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, roc_auc_score, classification_report, confusion_matrix
from sklearn.preprocessing import label_binarize
from train_model import CATEGORICAL
from utils import configure_logging, save_json


def metrics(y_true, y_pred, probabilities, classes):
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average="macro", zero_division=0)
    y_bin = label_binarize(y_true, classes=classes)
    auc = roc_auc_score(y_bin, probabilities, average="macro", multi_class="ovr")
    return {"accuracy":accuracy_score(y_true,y_pred),"macro_precision":precision,"macro_recall":recall,"macro_f1":f1,"roc_auc_ovr_macro":auc,"confusion_matrix":confusion_matrix(y_true,y_pred,labels=classes).tolist(),"classes":list(classes)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--models-dir", default="models")
    parser.add_argument("--reports-dir", default="reports")
    args = parser.parse_args(); configure_logging(); models=Path(args.models_dir); reports=Path(args.reports_dir); reports.mkdir(exist_ok=True)
    split=joblib.load(models/"evaluation_split.joblib"); X_test,y_test=split["X_test"],split["y_test"]
    baseline=joblib.load(models/"baseline_logistic_regression.joblib"); bp=baseline.predict(X_test); bprob=baseline.predict_proba(X_test)
    advanced=CatBoostClassifier(); advanced.load_model(models/"advanced_catboost.cbm"); ap=advanced.predict(X_test).ravel(); aprob=advanced.predict_proba(X_test)
    payload={"baseline_logistic_regression":metrics(y_test,bp,bprob,baseline.classes_),"advanced_catboost":metrics(y_test,ap,aprob,advanced.classes_)}
    save_json(payload,reports/"model_metrics.json")
    save_json(classification_report(y_test,bp,output_dict=True,zero_division=0),reports/"classification_report_baseline.json")
    save_json(classification_report(y_test,ap,output_dict=True,zero_division=0),reports/"classification_report_catboost.json")


if __name__ == "__main__": main()
