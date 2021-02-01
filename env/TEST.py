#  this creates the items
@app.route('/create-item', methods=['GET', 'POST'])
def create_item():
    if request.method == 'POST' and 'newitem' in request.form:
        if 'loggedin' in session:
            item_message = request.form['newitem']
            item_date = datetime.utcnow().isoformat()
            item_by = session['username']
        else:
            return render_template('index.html')
        # need to create add items for the inventory
    return redirect(url_for('index'))


@app.route('/item/<item_id>', methods=['GET', 'POST'])
def item(item_id):
    session['current_page'] = 'item'
    session['item_id'] = item_id
    login_status = '0'
    if 'loggedin' in session:
        login_status = '1'
    data = get_item_page_data(item_id=int(item_id))
    return render_template('item.html', login_status=login_status, data=data)
