import (
	    "github.com/bigkevmcd/go-configparser"
	)

p, err := configparser.NewConfigParserFromFile("cfg.ini")
if err != nil {
		     ...
}

v, err := p.Get("section", "option")
err = p.Set("section", "newoption", "value")

s := p.Sections()

v, err := p.GetInterpolated("mysql, host")

