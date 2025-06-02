from db import create_table, add_transaction, view_trans, view_trans_by_date
import argparse

def main():
    create_table()
    print("✅ App initialized.")

    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # أمر add
    add_parser = subparsers.add_parser("add", help="Add a new transaction")
    add_parser.add_argument("type", choices=["income", "expense"], help="Type of transaction")
    add_parser.add_argument("amount", type=float, help="Amount")
    add_parser.add_argument("category", help="Category")
    add_parser.add_argument("date", help="Date in yyyy-mm-dd format")
    add_parser.add_argument("description", help="Description")

    # أمر view
    view_parser = subparsers.add_parser("view", help="View all transactions")

    # أمر filter
    filter_parser = subparsers.add_parser("filter", help="Filter transactions by date")
    filter_parser.add_argument("start_date", help="Start date (yyyy-mm-dd)")
    filter_parser.add_argument("end_date", help="End date (yyyy-mm-dd)")
    
    # أمر summary
    simmary_parser=subparsers.add_parser("summary",help="summary")

     
    # أمر chart
    chart_parse=subparsers.add_parser("chart",help="show pie chart")

    # ⬅️ بعد كل أوامر subparsers
    args = parser.parse_args()

    if args.command == "add":
        add_transaction(args.type, args.amount, args.category, args.date, args.description)
        print(f"✅ {args.type.title()} of {args.amount} added.")

    elif args.command == "view":
        view_trans()

    elif args.command == "filter":
        view_trans_by_date(args.start_date, args.end_date)
    
    elif args.command=="summary":
        from db import summary
        summary()
    elif args.command=="chart":
        from db import plot_summary
        plot_summary()

if __name__ == "__main__":
    main()
