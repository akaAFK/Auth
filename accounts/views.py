from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def auth_view(request):

    if request.method == "GET":

        register_form = UserCreationForm()

        login_form = AuthenticationForm()

        saved_username = request.COOKIES.get("last_username", "")

        return render(
            request,
            "accounts/auth.html",
            {
                "register_form": register_form,
                "login_form": login_form,
                "saved_username": saved_username,
                "active_tab": "login",
            }
        )

    action = request.POST.get("action")


    if action == "register":

        register_form = UserCreationForm(request.POST)
        login_form = AuthenticationForm()

        if register_form.is_valid():

            user = register_form.save()

            login(request, user)

            response = redirect("auth")

            response.set_cookie(
                "last_username",
                user.username,
                max_age=60 * 60 * 24 * 30,
                httponly=True,
                samesite="Lax",
            )

            return response


    elif action == "login":

        register_form = UserCreationForm()

        login_form = AuthenticationForm(
            request=request,
            data=request.POST
        )

        if login_form.is_valid():

            user = login_form.get_user()

            login(request, user)

            response = redirect("auth")

            response.set_cookie(
                "last_username",
                user.username,
                max_age=60 * 60 * 24 * 30,
                httponly=True,
                samesite="Lax",
            )

            return response


    saved_username = request.COOKIES.get("last_username", "")

    return render(
        request,
        "accounts/auth.html",
        {
            "register_form": register_form,
            "login_form": login_form,
            "saved_username": saved_username,
            "active_tab": action,
        }
    )


@require_http_methods(["POST"])
def logout_view(request):

    logout(request)

    response = redirect("auth")

    response.delete_cookie("last_username")

    return response