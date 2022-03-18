
class TodoApp extends React.Component {
    constructor(props) {
      super(props);
      this.state = { items: [], text: '' };
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    render() {
      return (
        <div>
          <center>
            <h1>TODO</h1>
            <TodoList items={this.state.items} />
            <form onSubmit={this.handleSubmit}>
                <label htmlFor="new-todo">
                Что нужно сделать?
                </label>
                <input
                id="new-todo"
                onChange={this.handleChange}
                value={this.state.text}
                />
                <button>
                Add #{this.state.items.length + 1}
                </button>
            </form>
          </center>
        </div>
      );
    }
  
    handleChange(e) {
      this.setState({ text: e.target.value });
    }
  
    handleSubmit(e) {
      e.preventDefault();
      if (this.state.text.length === 0) {
        return;
      }
      const newItem = {
        text: this.state.text,
        id: Date.now()
      };
      this.setState(state => ({
        items: state.items.concat(newItem),
        text: ''
      }));
    }
  }
  
  class TodoList extends React.Component {
    render() {
      return (
        <ul>
          {this.props.items.map(item => (
            <font color="red" size="5">
                <li key={item.id}>
                    {item.text}
                </li>
            </font>
          ))}
        </ul>
      );
    }
  }
  
  ReactDOM.render(
    <TodoApp />,
    document.getElementById('app')
  );