from rest_framework import serializers

from applications.post.models import Shoes, Comment, Rating, Like, ShoesImage


class ShoesImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoesImage
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = '__all__'


class ShoesSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.email')
    comments = CommentSerializer(many=True, read_only=True)
    images = FilmImageSerializer(many=True, read_only=True)

    class Meta:
        model = Shoes
        fields = '__all__'


    def create(self, validated_data):
        post = Shoes.objects.create(**validated_data)
        request = self.context.get('request')
        fiels = request.FILES

        image_objects = []

        for file in fiels.getlist('images'):
            image_objects.append(ShoesImage(post=post, image=file))
            # PostImage.objects.create(post=post, image=file)

        ShoesImage.objects.bulk_create(image_objects)

        return post

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['like_count'] = instance.likes.filter(is_like=True).count()

        rating_result = 0
        for rating in instance.ratings.all():
            rating_result += rating.rating

        if rating_result:
            rep['rating'] = rating_result / instance.ratings.all().count()
        else:
            rep['rating'] = 0
        return rep






class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ('rating',)
