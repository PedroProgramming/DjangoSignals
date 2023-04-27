from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Pessoa, Historico

@receiver(post_save, sender=Pessoa)
def envia_sinal(sender, instance, created, **kwargs):
    if not created:
        x = Historico(nome=instance.nome,
                    email=instance.email,
                        telefone=instance.telefone,
                        pessoa=instance)
        x.save()
    else:
        print('Criado com sucesso')
