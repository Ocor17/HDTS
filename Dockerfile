FROM python
COPY ./HDTS-Django ./Django
COPY requirements.txt .
#EXPOSE 80
#EXPOSE 443
#EXPOSE 8000

#ENV DB_USERNAME=$DB_USERNAME
#ENV DB_PASSWORD=$DB_PASSWORD
#ENV DB_NAME=$DB_NAME
#ENV DB_HOST=$DB_HOST
#ENV PORT=$PORT
#ENV SECRET_KEY=$SECRET_KEY
#ENV ALLOWED_HOST=$ALLOWED_HOST
#ENV CSRF_TRUSTED_ORIGINS=$CSRF_TRUSTED_ORIGINS

RUN pip install -r requirements.txt
#RUN pip install Django\
#    pip install djongo\
#    pip install pytz\
#    pip install django-crispy-forms\
#    pip install django-filter
    
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
#RUN mkdir Django
RUN ls
#CMD ["python","Django/manage.py","createsuperuser", "--username=admin","--first_name=admin","--password=admin","--email=admin@admin.com"]
CMD ["python","Django/manage.py","runserver", "0.0.0.0:8000"]
