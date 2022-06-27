from groups.models import Group
from features.models import Feature

"""
This function will validate whether or not the group exists
and the feature. If the group or feature exists, it will return
the existing group or feature, otherwise it will create.
"""

class Helper:
    
    def get_or_create_group(search_group):
        group = []
        
        try:
            group = Group.objects.get(name=search_group["name"])
        except Group.DoesNotExist:
            group = Group.objects.create(**search_group)
        
        return group

    def get_or_create_features(features):
        characterist_list = []
        
        for feature in features:
            
            try:
                feature_value = Feature.objects.get(name=feature["name"])
                characterist_list.append(feature_value)
            except Feature.DoesNotExist:
                feature_value = Feature.objects.create(**feature)
                characterist_list.append(feature_value)
        
        return characterist_list

