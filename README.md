# ExtractLoadFactory

This application provides a generic procedure to extract and load data from a variety of SQL tables. It utilizes the factory design pattern to create worker objects as needed, and can be executed via a cron job or another automated job scheduler. 

Care was taken to adhere to SOLID design principles, but there are a few violations (hardcoded SQL statements in the extractor and loader objects, for example). 

The app can be easily extended by adding additional ConcreteFactories. In addition, functionality can be expanded by building transformer and validator objects for a complete ETL factory.
