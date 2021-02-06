from amazon.api import AmazonAPI
# amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
amazon = AmazonAPI('AKIAJBKVZWMNWVBZM6SQ','ZRvDFaGr5MbthzWjKuLWDqfoCozaOIixGgvdm4h/', '149652593468')
# product = amazon.aws_associate_tag  	B016QBSXRS
# amazon = AmazonAPI(locale='IN')
items = amazon.search(Publisher="O'Reilly")
for item in items:
    try:
        print(item.price_and_currency)
    except Exception:
        continue