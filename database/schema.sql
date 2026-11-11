CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Email TEXT UNIQUE
);

CREATE TABLE Accounts (
    AccountID INTEGER PRIMARY KEY,
    UserID INTEGER,
    AccountName TEXT,
    Balance REAL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

CREATE TABLE Categories (
    CategoryID INTEGER PRIMARY KEY,
    CategoryName TEXT
);

CREATE TABLE Transactions (
    TransactionID INTEGER PRIMARY KEY,
    AccountID INTEGER,
    CategoryID INTEGER,
    Amount REAL,
    TransactionDate DATE,
    Description TEXT,
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

CREATE TABLE Budgets (
    BudgetID INTEGER PRIMARY KEY,
    UserID INTEGER,
    CategoryID INTEGER,
    MonthlyLimit REAL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);