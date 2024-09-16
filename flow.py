from promptflow import FlowRunner

def main():
    runner = FlowRunner()
    result = runner.run(flow="hello_world")
    print(result)

if __name__ == "__main__":
    main()