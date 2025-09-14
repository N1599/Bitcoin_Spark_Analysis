# Bitcoin\_Spark\_Analysis

Analyzed the data from coingecko api using apache spark and airflow dags . Generated pdf for assessing bitcoin metrics.





**Features -** 


\- Apache Airflow DAGs for data processing

\- Spark for large-scale data analysis

\- Dockerized environment for easy setup

\- Python dependencies managed via `requirements.txt`

\- Java 17 installed for Spark support



**Workflow -** 

1. Start the DAG in Airflow.
2. Coingecko API fetches the data.
3. Spark Transformations for processing and analysis.
4. PDF report gets generated.





**Setup -** 
1. **Clone the repository** - 
```bash
git clone https://github.com/N1599/Bitcoin_Spark_Analysis.git
cd Bitcoin_Spark_Analysis



2\. **Build docker images** - docker compose build --no-cache



3\. **Start the containers** - docker compose up -d



4\. **Initialize Airflow DB (first run)** - docker compose exec airflow-webserver airflow db init



5\. **Access the Airflow UI** - Open http://localhost:8080 in your browser and start running the DAG.



6\. See the output generated in the **outputs/** folder.

