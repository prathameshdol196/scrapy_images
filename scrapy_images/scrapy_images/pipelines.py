# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline

class CustomImagePipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):

        # Get the image name from the item
        image_name = item.get('name')
        # Replace the original image name with the extracted one
        return f'full/{image_name}'


