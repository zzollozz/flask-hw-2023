

def is_valid_form_fields(request):
    for val in request.form.items():
        if not val[1]:
            return True

