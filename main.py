from typing import List

class Person:
  def __init__(self, name: str, lastname: str, group: int, team: int):
    self.__name = name
    self.__lastname = lastname

    self.setGroup(group)
    self.setTeam(team)

  # El nombre y el apellidos son inmutables para la mayoria de logicas de negocio
  # Por lo que se restringe el acceso a dichas props 

  def getName(self) -> str:
    return self.__name

  def getLastname(self) -> str:
    return self.__lastname
  
  # El grupo y el equipo pueden tener varias validaciones lógicas 
  # por eso los setters y getters

  def setGroup(self, group: int):
    if group < 11:
      raise ValueError("El número del grupo debe ser como mínimo 11")

    group = str(group)

    if len(group) != 2:
      raise ValueError("El grupo debe tener 2 cifras")

    if int(group[0]) > 4:
      raise ValueError("El grupo empieza por el año por lo que la primera cifra no puede ser mayor que 4")

    if int(group[1]) == 0:
      raise ValueError("El segundo dígito del grupo debe ser mayor que 0")

    self.__group = group

  def getGroup(self) -> int:
    return self.__group
  
  def setTeam(self, team: int):
    if team < 1:
      raise ValueError("El número del equipo debe ser como mínimo 1")

    self.__team = team

  def getTeam(self) -> int:
    return self.__team

  def __repr__(self) -> str:
    return f"{self.__name} {self.__lastname} del grupo {self.__group} y del equipo {self.__team}"

def print_stylistic_list[T](title: str, items: List[T]):
  first_character = "┌"
  in_between_char = "│"
  final_character = "└"
  list_decorator = "◊"

  size = len(items)

  print(f"{first_character} {title}")

  for value in items:
    print(f"{in_between_char} {list_decorator} {value}")

  print(f"{final_character} {size} elemento{ "" if size == 1 else "s" }")

try:
  # Estos son los datos de los integrantes del equipo
  people = [
    Person(name="Brian", lastname="Monteagudo Pérez", group=-21, team=5),
    Person(name="Javier David", lastname="Coroas Cintra", group=21, team=5),
  ]
  
  print_stylistic_list("Personas registradas", people)

except ValueError as error:
  (error_message, *_) = error.args
  print(error_message)
