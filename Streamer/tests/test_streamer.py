import  data_factory
from Streamer import Streamer
from Activity import Activity
from utils import Comparator

data_set_path = "/home/ehud/Desktop/dataset"
activities = []
activity_paths = data_factory.produce(data_set_path)
total_predicted = 0
total_PP = 0
total_video_related = 0
for threshold in [500,1500,2500,3500,4500,6000,7000,10000]:
    total_predicted = 0
    total_PP = 0
    total_video_related = 0
    print('curr threshold',threshold)
    for activity_path in activity_paths:
        if activity_path.path.find('youtube') != -1:
            curr_activity = Activity(activity_path)
            print(curr_activity.activity_path.path)
            results = (Streamer(curr_activity, threshold).get_video_related_streams())
            get_sni_csv_path = (curr_activity.activity_path.get_sni_csv_path())
            triple = Comparator.compare(get_sni_csv_path, results)
            total_predicted += triple[2]
            total_PP += triple[0]
            total_video_related += triple[1]
            curr_activity = None
    print('total accuracy = %',total_PP/total_video_related)
    print('total presicion = $', total_PP/total_predicted)