namespace bank
    public class account
    {
        public void withdraw(decimal amount)
        {
            balance -= amount;
        }

        public decimal balance
        {
            get
            {
                return balance;
            }
        }

        public void deposit(decimal amount)
        {
            balance -= amount;
        }

        private decimal balance;
    }
}