## OOP Principles and Design Patterns and SOLID Principles

This project is built with Flask, it is a micro web framework for Python. However, I still try to apply OOP principles and design patterns to make the code more flexible and easy to understand. 

The idea is to make the project modular and easy to extend. Each module has its own responsibility and is designed to be independent. 

For example: Module `swatches` is responsible for handling the color swatch related logic. It contains the following files:

File: `interfaces/color_swatch.py` is an abstract class that defines the structure for a color swatch. It is used as a base class for all color swatch types. Help developer to enforce the structure of a color swatch. Keep the code clean and easy to understand. 

File: `repositories/swatch_repository.py` is a repository that handles the data access layer. It is used to abstract the data source from the business logic. Aka this serve as a bridge between the data source and the business logic. 

File: `strategies/` is a folder that contains the implementation of the color swatch types. Each strategy is a class that implements the `ColorSwatch` interface. Make the code more flexible and easy to extend. Adding new color swatch type is as easy as adding a new strategy.

File: `controllers/swatch_controller.py` is a controller that handles the request and response. It is a single entry point for all the requests.  

File: `tests/` is a folder that contains the test cases for the project. It is used to test the project and make sure the project is working as expected.  

