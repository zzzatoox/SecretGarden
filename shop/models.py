from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from unidecode import unidecode


class Category(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название", help_text="Введите название категории"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
        help_text="Введите название подкатегории",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name="Категория",
        help_text="Выберите категорию подкатегории",
    )

    def __str__(self):
        return f"{self.category.title} - {self.title}"

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Product(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название", help_text="Введите название цветка"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание цветка",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        default=1,
        verbose_name="Категория",
        help_text="Выберите категорию цветка",
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Подкатегория",
        help_text="Выберите подкатегорию цветка (необязательно)",
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        verbose_name="Слаг",
        help_text="Слаг генерируется автоматически",
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена", help_text="Введите цену цветка"
    )
    sale_price = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Цена со скидкой",
        help_text="Введите цену цветку со скидкой (необязательно)",
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name="В наличии",
        help_text="Отметьте, если продукт доступен",
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата создания заполняется автоматически",
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_base = slugify(unidecode(self.title))
            slug = slug_base

            while Product.objects.filter(slug=slug).exists():
                slug = f"{slug_base}-{get_random_string(5)}"

            self.slug = slug
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Цветок"
        verbose_name_plural = "Цветы"
