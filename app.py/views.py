



@app.route('/delete/<int:id>')
def delete(id):
    cart_item_to_delete = post.query.get_or_404(id)

    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect('/cart')
    except:
        return "There was a problem removing that item from your cart"