# Clean Architecture Python



This example is heavily inspired by:

[clean-architecture-example By Mattia Battiston](https://github.com/mattia-battiston/clean-architecture-example)

[Enforcing SRP By Sobolevn](https://sobolevn.me/2019/03/enforcing-srp)



## Run project

```shell
git clone https://github.com/phakiller/clean-architecture-python
cd clean-architecture-python
pipenv install
```



#### With Flask

```shell
export FLASK_APP="$(pwd)/example/boot.py"
flask initdb
flask run
```

**Routes**

- /health/status
- /broadbandaccessdevice/<hostname>/



## Improves

*Did you find improvements to make?*

Open an Issue or submit your Pull Request



## TODO

- [ ] Use [mappers](https://github.com/dry-python/mappers/blob/master/docs/index.md) to translate Domain to Model objects and vice versa, instead create **to_entity(...)** method in Model classes
- [ ] Write more unit tests