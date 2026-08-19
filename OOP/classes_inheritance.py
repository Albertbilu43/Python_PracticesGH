# Databricks notebook source
# MAGIC %md
# MAGIC ##### TBD

# COMMAND ----------

# DBTITLE 1,Cell 1
class Level1:
    variable_1 = 100
    def __init__(self, nivel1):
        self.nivel1= nivel1
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200
    def __init__(self, nivel1, nivel2):
        super().__init__(nivel1)
        self.nivel2= nivel2
        self.var_2 = 201
        
    
    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300
    def __init__(self, nivel1, nivel2, nivel3):
        super().__init__( nivel1, nivel2)
        self.nivel3= nivel3        
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3(1,2,3)

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())
    

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Inheritance is not the only way to construct adaptable classes. 
# MAGIC #### You can achieve the same goals (not always, but very often) by using a technique named COMPOSITION.
# MAGIC
# MAGIC Composition is the process of composing an object using other different objects. The objects used in the composition deliver a set of desired traits (properties and/or methods) so we can say that they act like blocks used to build a more complicated structure.
# MAGIC
# MAGIC It can be said that:
# MAGIC
# MAGIC -     inheritance extends a class's capabilities by adding new components and modifying existing ones; in other words, the complete recipe is
# MAGIC       contained inside the class itself and all its ancestors; the object takes all the class's belongings and makes use of them;
# MAGIC -     composition projects a class as a container able to store and use other objects (derived from other classes) where each of the objects
# MAGIC       implements a part of a desired class's behavior.
# MAGIC

# COMMAND ----------

