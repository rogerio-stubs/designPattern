from singleton import Singleton
if __name__ == "__main__":
  s1 = Singleton()
  s2 = Singleton()

  if id(s1) == id(s2):
    print("Singleton works, both variables contain the same instance.")
  else:
    print("Singleton failed, variables contain different instances.")