# Computer Basics - Applied ML Projects

This repository contains a collection of computer science fundamentals and applied machine learning projects developed as part of the Rebelway Applied ML course. The projects demonstrate core programming concepts, data structures, object-oriented programming, and numerical computing practices.

## 📁 Project Structure

### 🛒 Shopping Cart System
A comprehensive e-commerce cart management system built with Python, demonstrating:

**Features:**
- **Item Management**: Create and manage items with name, type, and price
- **Cart Operations**: Add items, remove by query, calculate totals
- **Search Functionality**: Find items by name or type
- **Data Persistence**: JSON-based database storage
- **Interactive Selection**: Remove items through user selection interface

**Key Components:**
- `Item` class: Immutable dataclass with price rounding and search capabilities
- `Cart` class: Main cart management with CRUD operations
- `Fstream` class: File I/O operations for JSON data handling
- `RandomUtils` class: Generate unique 6-character IDs

**Technologies:** Python dataclasses, JSON file handling, pytest testing

### 📚 Library Management System
A book library system adapted from the shopping cart architecture, featuring:

**Features:**
- **Book Management**: Add books with title, author, genre, and availability status
- **Library Operations**: Search, checkout, return books
- **Duplicate Prevention**: Prevents adding books with same title and author
- **Availability Tracking**: Monitor checked-out vs available books
- **Data Persistence**: JSON database with book records

**Key Components:**
- `Book` class: Immutable dataclass with search string and status properties
- `LibrarySystem` class: Core library operations and book management
- Enhanced duplicate checking logic
- Comprehensive availability management

**Technologies:** Python dataclasses, JSON persistence, pytest testing

### 🔢 Numerical Computing Practices

#### NumPy Fundamentals (`numpy/`)
**np_practice.ipynb:**
- Array creation with `np.arange()`
- Array slicing and indexing operations
- In-place array modifications
- Array copying vs view behavior
- 2D array manipulation
- Zero array initialization

**np_02.ipynb:**
- Array creation from Python lists
- Matrix multiplication using `dot()` method
- Conditional operations with `np.where()`
- Advanced array transformations

#### JAX Introduction (`jax/`)
**jax_intro.ipynb:**
- **Neural Network Functions**: Implementation of ReLU, Softmax, Cross-entropy
- **Random Number Generation**: JAX PRNG key management and random arrays
- **JIT Compilation**: Performance optimization with `@jit` decorator
- **Advanced Activations**: SELU activation function implementation
- **Performance Benchmarking**: Timing comparisons between regular and JIT-compiled functions
- **Matrix Operations**: Optimized matrix multiplication with performance analysis

## 🧪 Testing Practices

Both systems include comprehensive test suites demonstrating:
- **Unit Testing**: Individual component testing with pytest
- **Fixture Usage**: Temporary database creation for isolated tests
- **Property Testing**: Validation of object properties and behaviors
- **Integration Testing**: End-to-end functionality verification
- **Test Coverage**: Core functionality and edge cases

## 🚀 How to Run

### Shopping Cart System
```bash
cd shopping_cart
python main.py
```

### Library System
```bash
cd library
python main.py
```

### Run Tests
```bash
# Shopping cart tests
cd shopping_cart
python -m pytest tests/ -v

# Library system tests
cd library
python -m pytest tests/ -v
```

### Jupyter Notebooks
```bash
# Start Jupyter and open notebooks
jupyter notebook numpy/np_practice.ipynb
jupyter notebook numpy/np_02.ipynb
jupyter notebook jax/jax_intro.ipynb
```

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **Dataclasses**: Modern Python data structure implementation
- **JSON**: Data persistence and serialization
- **pytest**: Testing framework
- **NumPy**: Numerical computing and array operations
- **JAX**: High-performance machine learning computations
- **Jupyter Notebooks**: Interactive development and experimentation

## 📋 Requirements

```
pytest
numpy
jax
jupyter
```

## 🎯 Learning Objectives

This repository demonstrates proficiency in:
- Object-oriented programming principles
- Data structure design and implementation
- File I/O and data persistence
- Test-driven development practices
- Numerical computing with NumPy
- High-performance computing with JAX
- Code organization and project structure
- Documentation and README best practices

## 📝 Key Programming Concepts Covered

- **Immutable Data Structures**: Using frozen dataclasses
- **Property Decorators**: Clean attribute access patterns
- **Context Managers**: Safe file handling
- **Exception Handling**: Robust error management
- **Type Hints**: Modern Python typing practices
- **Modular Design**: Separation of concerns and reusable components
- **Performance Optimization**: JIT compilation and benchmarking
