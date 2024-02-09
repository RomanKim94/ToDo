class TaskServices:

    @staticmethod
    def filter_by_name(qs, name):
        return qs.filter(name__contains=name)

    @staticmethod
    def filter_by_priority(qs, priority):
        return qs.filter(priority=priority)

    @staticmethod
    def filter_by_stage(qs, stage):
        return qs.filter(stage=stage)

    @staticmethod
    def qs_filter(qs, params, person):
        if not person.is_staff:
            qs = qs.filter(list__person=person)
        priority = params.get('priority')
        if priority:
            qs = TaskServices.filter_by_priority(qs, priority)
        name = params.get('name')
        if name:
            qs = TaskServices.filter_by_name(qs, name)
        stage = params.get('stage')
        if stage:
            qs = TaskServices.filter_by_stage(qs, stage)
        return qs

    @staticmethod
    def qs_sorting(qs, params):
        sorting_list = [
            'name',
            'priority',
            'create_time',
            'update_time',
        ]
        sorting_list.extend(['-' + word for word in sorting_list])
        sorting = params.get('sorting_by')
        if sorting in sorting_list:
            qs = qs.order_by(sorting)
        else:
            qs = qs.order_by('update_time')
        return qs
