from backend.components.dataIngestion import DataIngestion


leageus= ['epl ','d1','italy','s0','sp1']


def main():
    for league in leageus:
        obj=DataIngestion(league=league)
        obj.initiate_data_ingestion()
        


if __name__ == "__main__":
    main()