from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class Curso:
    def __init__(self):
        self.cursos = []
        self.next_id = 7

    def get_curso(self):
        return self.cursos

    def get_curso_id(self, curso_id):
        for curso in self.cursos:
            if curso['id'] == curso_id:
                return curso
        return None

    def post_curso(self, nome):
        novo_curso = {
            'id': self.next_id,
            'nome': nome
        }
        self.cursos.append(novo_curso)
        self.next_id += 1
        return novo_curso

    def put_curso(self, curso_id, novo_nome):
        for curso in self.cursos:
            if curso['id'] == curso_id:
                curso['nome'] = novo_nome
                return curso
        return None

    def delete_curso(self, curso_id):
        for curso in self.cursos:
            if curso['id'] == curso_id:
                self.cursos.remove(curso)
                return True
        return False

curso_manager = Curso()


curso1 = curso_manager.post_curso("Intensivão de Culinaria")
curso2 = curso_manager.post_curso("Aprendendo a Desenvolver")


print(curso_manager.get_curso())


print(curso_manager.get_curso_id(7))


curso_manager.put_curso(7,"Aprendendo a jogar game maker")


curso_manager.delete_curso(8)


print(curso_manager.get_curso())
