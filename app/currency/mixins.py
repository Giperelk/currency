from django_filters.views import FilterView


class ModifiedPagesMixin:

    def get_context_data(self, object_list=None, **kwargs):
        context = super(FilterView, self).get_context_data(object_list=object_list, **kwargs)
        context['prev_end_page'] = context['paginator'].num_pages-1
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context
