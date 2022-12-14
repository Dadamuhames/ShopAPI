from rest_framework import serializers
from .models import Products, ProductVariants, Category, ProductImages, Atributs, AtributOptions, Color, Comments
import django_filters.rest_framework as filter
from .filters import ProductVariantFilter


# for product img
class ProductImageSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ProductImages
        fields = ['image']




# for color
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

# for product
class ProductSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True)

    class Meta:
        model = Products
        fields = '__all__'


# for atributs
class AtributOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtributOptions
        fields = ['name', 'id']


# for atribut options
class AtributSerializer(serializers.ModelSerializer):
    options = AtributOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = Atributs
        fields = '__all__'


# for product variant
class ProductVariantSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    images = ProductImageSerializer(read_only=True, many=True)


    class Meta:
        model = ProductVariants
        fields = ['id', 'product', 'price', 'qty', 'images', 'color']

    
    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['img_first'] = ProductImageSerializer(instance.images.first()).data

        data['atributs'] = []
        
        for opt in instance.options.all():
            atribut = opt.atribut
            data['atributs'].append({
                'name': atribut.name,
                'option': opt.name
            })

        return data


# for single category(used to show children categories)
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'icon']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['count'] = instance.products.count()

        return data


# Home Page Serializer
class HomePageSerializer(serializers.Serializer):
    products = ProductVariantSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    brands = CategorySerializer(many=True, read_only=True)
    hits = ProductVariantSerializer(many=True, read_only=True)
    product_of_day = ProductVariantSerializer()



# Coralog Serializer
class CotalogSerializer(serializers.Serializer):
    products = ProductVariantSerializer(many=True, read_only=True)
    hit_products = ProductVariantSerializer(many=True, read_only=True)


class ReqursiveCategorySerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


# Serializer for category with no parent
class CtegoryDeteilSerializer(serializers.ModelSerializer):
    children = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'inf', 'children', 'icon', 'image']


class CategoryParentSerializer(serializers.Serializer):
    def to_representation(self, value):
        data = {}
        data['id'] = value.id
        data['name'] = value.name
        data['icon'] = value.icon
        data['parent'] = CategoryParentSerializer(value.parent).data

        return data


class ProductVeriantRepresent(serializers.Serializer):
    def to_representation(self, instance):
        data = instance.get_default()

        serializer = ProductVariantSerializer(data).data

        return serializer 



class CategoryProductsSerializer(serializers.ModelSerializer):
    children = CategorySerializer(many=True, read_only=True)
    products = ProductVeriantRepresent(many=True)
    parent = CategoryParentSerializer()
    atributs = AtributSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


        
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        exclude = ['product']



class ProductVeriantDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    color = ColorSerializer()
    comments = CommentsSerializer(many=True)

    class Meta: 
        model = ProductVariants
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        atributs = instance.product.category.get(children=None).atributs.all()
        data['atributs'] = []

        for atr in atributs:
            atr_data = AtributSerializer(atr).data
            options = atr_data['options']
            
            opt_lst = [it for it in instance.options.all()]

            for opt in opt_lst:
                if opt.atribut == atr:
                    opt_lst.remove(opt)

            for opt in options:
                lst = opt_lst.copy()
                opshn = AtributOptions.objects.get(id=opt['id'])             
                lst.append(opshn)
                id_lst = [it.id for it in lst]
                
                variant = ProductVariants.objects.filter(color=instance.color)
                for id in id_lst:
                    variant = variant.filter(options=id)

                if variant.count() == 0: 
                    opt['variant'] = None
                else:
                    opt['variant'] = variant.first().id
        

            data['atributs'].append(atr_data)

        colors = instance.product.colors.all()
        data['colors'] = []

        for color in colors:
            serializer = ColorSerializer(color).data
            variant = ProductVariants.objects.filter(color=color)

            for opt in instance.options.all():
                variant.filter(options=opt)

            if variant.count() == 0:
                serializer['variant'] = None
            else:
                serializer['variant'] = variant.first().id

            data['colors'].append(serializer)

        return data



class AllCetegories(serializers.ModelSerializer):
    children = ReqursiveCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['name', 'children', 'id', 'icon']



class CartSerializer(serializers.Serializer):
    def to_representation(self, instance):
        data = []

        for item in instance:
            variant = ProductVariants.objects.get(id=item['variant'])
            it = {it: item[it] for it in item}
            it['variant'] = ProductVariantSerializer(variant).data
            data.append(it)

        return data


class CartViewSerializer(serializers.Serializer):
    cart = CartSerializer()

    def to_representation(self, instance):
        data = super().to_representation(instance)

        total = 0
        for it in instance['cart']:
            total += float(it['price'])

        data['total'] = total
        data['count'] = len(instance['cart'])

        return data


class WishItemSerializer(serializers.Serializer):
    def to_representation(self, instance):
        data = []
        for i in range(len(instance)):
            if type(instance[i]) is str:
                product = ProductVariants.objects.get(id=instance[i])
                data.append(ProductVariantSerializer(product).data)

        return data


# wishlist serializer
class WishlistSerializer(serializers.Serializer):
    list = WishItemSerializer()