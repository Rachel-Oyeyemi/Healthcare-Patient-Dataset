.PHONY: install data preprocess features train evaluate app test pipeline presentation
install:
	pip install -r requirements.txt
data:
	python src/download_data.py
preprocess:
	python src/preprocess.py
features:
	python src/feature_engineering.py
train:
	python src/train_model.py
evaluate:
	python src/evaluate_model.py
app:
	streamlit run app/app.py
test:
	pytest -q
pipeline:
	python run_pipeline.py
presentation:
	python presentation/create_presentation.py
