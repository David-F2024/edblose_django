from django.db import models

class TUser(models.Model):

    code = models.CharField(
        max_length=5,
        db_column="CD_USER"
    )
    email = models.EmailField(
        max_length=50,
        db_column="MAIL_USER"
    )

    password = models.CharField(
        max_length=50,
        db_column="MDP"
    )

    nom = models.CharField(
        max_length=50,
        db_column="NM_USER",
        blank=True,
        null=True
    )

    prenom = models.CharField(
        max_length=50,
        db_column="PRN_USER",
        blank=True,
        null=True
    )

    date_connexion = models.DateTimeField(
        db_column="DT_TC_CNX",
        auto_now=True
    )

    class Meta:
        managed = False   #
        db_table = "t_user"

