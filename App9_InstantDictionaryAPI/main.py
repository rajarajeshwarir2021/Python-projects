import api
import documentation
import justpy as jp


jp.Route("/", documentation.Doc.serve)
jp.Route("/api", api.Api.serve)

jp.justpy()
