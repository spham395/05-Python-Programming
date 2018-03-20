# OOP Principles

---

Capturing the essential internal state and methods that cause state change is the first step in good class design. We can summarize some helpful design principles using the acronym **S.O.L.I.D**.:

* **Single Responsibility Principle**
  : A class should have one clearly defined responsibility.
* **Open/Closed Principle**
  : A class should be open to extension-generally via inheritance, but closed to modification. We should design our classes so that we don't need to tweak the code to add or change features.
* **Liskov Substitution Principle**
  : We need to design inheritance so that a subclass can be used in place of the superclass.
* **Interface Segregation Principle**
  : When writing a problem statement, we want to be sure that collaborating classes have as few dependencies as possible. In many cases, this principle will lead us to decompose large problems into many small class definitions.
* **Dependency Inversion Principle**
  : It's less than ideal for a class to depend directly on other classes. It's better if a class depends on an abstraction, and a concrete implementation class is substituted for the abstract class.

The goal is to create classes that have the proper behavior and also adhere to the design principles.

