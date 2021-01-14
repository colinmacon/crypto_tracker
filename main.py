import cli
import data_pull
import filter_export

def main():
    c = cli.CLI()
    c.interface()
    c.set_values()
    o = filter_export.Operate(c)
    d = data_pull.Track()
    o.feed(d)


if __name__== "__main__":
  main()
