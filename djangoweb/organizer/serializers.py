from rest_framework.serializers import (
    #HyperlinkedIdentityField,
    HyperlinkedModelSerializer,
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedRelatedField,
    )
from .models import Tag, Startup, NewsLink
from rest_framework.reverse import reverse

class TagSerializer(HyperlinkedModelSerializer):
    #url = HyperlinkedIdentityField(
    #    lookup_field = "slug", view_name="api-tag-detail",
    #)
    class Meta:
        model = Tag
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-tag-detail",
            }
        }

class StartupSerializer(HyperlinkedModelSerializer):
    #tags = TagSerializer(many=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Startup
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-startup-detail"
            }
        }

'''

    def create(self, validated_data):
        """Create Startup and associate Tags"""
        tag_data_list = validated_data.pop("tags")
        startup = Startup.objects.create(**validated_data)
        #the code below, where we relate bulk-creates objects,
        #works only in databases that return PK after the bulk insert,
        #which at time of writing is only PostgreSQL
        tag_list = Tag.objects.bulk_create(
            [Tag(**tag_data) for tag_data in tag_data_list]
        )
        startup.tags.add(*tag_list)
        return startup
'''

class NewsLinkSerializer(ModelSerializer):
    """Serialize NewsLink data"""

    url = SerializerMethodField()
    #startup = StartupSerializer()
    startup = HyperlinkedRelatedField(
        queryset=Startup.objects.all(),
        lookup_field="slug",
        view_name="api-startup-detail",
    )

    class Meta:
        model = NewsLink
        fields = '__all__'
        exculde = ("id",)

    def get_url(self, newslink):
        """Build full URL for NewsLink API detail"""
        print("get_url() get called in serializer")
        return reverse(
            "api-newslink-detail",
            kwargs=dict(
                startup_slug=newslink.startup.slug,
                newslink_slug=newslink.slug,
            ),
            request=self.context["request"],
        )
'''
    startup = HyperlinkedRelatedField(
        queryset=Startup.objects.all(),
        lookup_field="slug",
        view_name="api-startup-detail",
    )

    class Meta:
        model = NewsLink
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-newslink-detail"
            }
        }
'''
