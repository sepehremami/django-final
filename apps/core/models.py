from django.db import models
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels
from django.contrib.auth.models import Group, Permission
from django.core.validators import RegexValidator


class BaseModel(models.Model):
    """
    Common attributes of all models
    All models extend BaseModel
    """

    is_deleted = models.BooleanField(default=False, editable=False)
    create_date = jmodels.jDateField(auto_now_add=True)
    modified_date = jmodels.jDateField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        super().delete()


class User(AbstractUser):
    """
    General User model
    Django auth user
    """
    phone_number = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^0\d{10}$',
                message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
            ),
        ],
    )


class AddressManager(models.Manager):
    """"""
    def get_default_address(self, user):
        try:
            address = self.get(user=user, is_default=True)
        except self.model.DoesNotExist:
            address = None

        return address


class Address(BaseModel):
    """
    Address that will be written when order is being shipped
    users can have many address
    for default address see AddressManager
    """
    user = models.ForeignKey('User', on_delete='CASCADE')
    receiver = models.CharField(max_length=24)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    addr = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=6, null=True)
    phone = models.CharField(max_length=11)
    is_default = models.BooleanField(default=False)

    objects = AddressManager()


class Membership(BaseModel):
    """
    defining memberships for users with benefits and offers
    """
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    discount_value = models.IntegerField()
    discount_unit = models.CharField(choices=[
        ('t', 'Toman'),
        ('p', 'Percent'),
    ])
    valid_until = jmodels.jDateTimeField()
    free_shipping = models.BooleanField(default=False)


class UserRewardLog(BaseModel):
    """
    log user reward activity
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reward_type = models.CharField(max_length=50)
    reward_point = models.IntegerField()
    operation_type = models.CharField(max_length=100)


